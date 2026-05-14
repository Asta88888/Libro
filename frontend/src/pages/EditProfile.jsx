import { useEffect, useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";
import "./profile.css";

export default function EditProfile() {
    const [form, setForm] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        api.get("users/me/")
            .then(res => setForm(res.data))
            .catch(err => console.log(err));
    }, []);

    function handleChange(e) {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        });
    }

    async function handleSubmit(e) {
        e.preventDefault();

        try {
            await api.patch("users/me_update/", form);
            navigate("/profile");
        } catch (err) {
            console.log(err);
        }
    }

    if (!form) return <div className="profile-loading">Loading...</div>;

    return (
        <div className="profile-page">

            <div className="profile-panel">

                <h1 className="edit-title">Редактирование профиля</h1>

                <form className="edit-form" onSubmit={handleSubmit}>

                    <input name="first_name" value={form.first_name || ""} onChange={handleChange} placeholder="Имя" />
                    <input name="last_name" value={form.last_name || ""} onChange={handleChange} placeholder="Фамилия" />
                    <input name="phone" value={form.phone || ""} onChange={handleChange} placeholder="Телефон" />
                    <input name="address" value={form.address || ""} onChange={handleChange} placeholder="Адрес" />

                    {/* 🔥 ДОБАВИЛИ ДАТУ */}
                    <input
                        type="date"
                        name="date_of_birth"
                        value={form.date_of_birth || ""}
                        onChange={handleChange}
                    />

                    <textarea
                        name="bio"
                        value={form.bio || ""}
                        onChange={handleChange}
                        placeholder="О себе"
                    />

                    <button type="submit" className="primary-btn">
                        Сохранить изменения
                    </button>

                </form>

            </div>

        </div>
    );
}