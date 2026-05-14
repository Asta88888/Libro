import { useEffect, useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";
import "./profile.css";

export default function Profile() {
    const [user, setUser] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        api.get("users/me/")
            .then((res) => setUser(res.data))
            .catch((err) => console.log("PROFILE ERROR:", err));
    }, []);

    if (!user) {
        return (
            <div className="profile-loading">
                Загрузка профиля...
            </div>
        );
    }

    return (
        <div className="profile-page">

            <div className="profile-panel">

                {/* HEADER */}
                <div className="profile-header">

                    <img
                        className="profile-avatar"
                        src={
                            user.image ||
                            `https://ui-avatars.com/api/?name=${user.email}&background=6d4c41&color=fff&size=256`
                        }
                        alt="avatar"
                    />

                    <div className="profile-info">

                        <h1>
                            {user.first_name || "Пользователь"}{" "}
                            {user.last_name || ""}
                        </h1>

                        <p className="profile-email">
                            @{user.email}
                        </p>

                        <div className="profile-meta">

                            <span className={`role-badge role-${user.role}`}>
                                {user.role}
                            </span>

                            <span className="member-since">
                                Участник с{" "}
                                {user.date_joined
                                    ? new Date(user.date_joined).toLocaleDateString()
                                    : "—"}
                            </span>

                        </div>

                    </div>
                </div>

                {/* BIO */}
                <div className="bio-card">

                    <span>О себе</span>

                    <p>
                        {user.bio || "Пользователь пока ничего не рассказал о себе"}
                    </p>

                </div>

                {/* STATS */}
                <div className="profile-stats">

                    <div className="stat-card">
                        <span>ID</span>
                        <h3>{user.id}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Email</span>
                        <h3>{user.email || "—"}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Имя</span>
                        <h3>{user.first_name || "—"}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Фамилия</span>
                        <h3>{user.last_name || "—"}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Телефон</span>
                        <h3>{user.phone || "—"}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Дата рождения</span>
                        <h3>{user.date_of_birth || "—"}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Адрес</span>
                        <h3>{user.address || "—"}</h3>
                    </div>

                    <div className="stat-card">
                        <span>Роль</span>
                        <h3>{user.role}</h3>
                    </div>

                </div>

                {/* ACTIONS */}
                <div className="profile-actions">

                    <button
                        className="primary-btn"
                        onClick={() => navigate("/profile/edit")}
                    >
                        Редактировать профиль
                    </button>

                    <button className="secondary-btn">
                        Мои книги
                    </button>

                </div>

            </div>

        </div>
    );
}