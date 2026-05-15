import { useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);

    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();

        console.log("LOGIN CLICKED");
        console.log("DATA:", { email, password });

        try {
            const response = await api.post("token/", {
                email: email.trim(),
                password: password,
            });

            console.log("SUCCESS:", response.data);

localStorage.setItem("access", response.data.access);
localStorage.setItem("refresh", response.data.refresh);

setError(null);

navigate("/");

        } catch (error) {
            console.log("LOGIN ERROR:", error.response?.data || error.message);

            setError(
                error.response?.data?.detail ||
                JSON.stringify(error.response?.data) ||
                "Ошибка логина"
            );
        }
    };

    return (
        <div className="container mt-5" style={{ maxWidth: "400px" }}>
            <h2>Вход</h2>

            <form onSubmit={handleLogin}>
                <input
                    className="form-control mb-2"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    className="form-control mb-2"
                    type="password"
                    placeholder="Пароль"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                {error && (
                    <div className="alert alert-danger">
                        {error}
                    </div>
                )}

                <button className="btn btn-primary w-100">
                    Войти
                </button>
            </form>
        </div>
    );
}
