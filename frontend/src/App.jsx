import { Routes, Route, Navigate } from "react-router-dom";

import Layout from "./layouts/Layout";
import Login from "./pages/Login";
import Profile from "./pages/Profile"; // 👈 ВАЖНО ДОБАВИТЬ

function Home() {
    return <h1>Главная</h1>;
}

function Books() {
    return <h1>Книги</h1>;
}

// защита маршрутов
function PrivateRoute({ children }) {
    const token = localStorage.getItem("access");
    return token ? children : <Navigate to="/login" />;
}

export default function App() {
    return (
        <Routes>

            <Route path="/login" element={<Login />} />

            {/* защищённая часть */}
            <Route
                path="/"
                element={
                    <PrivateRoute>
                        <Layout />
                    </PrivateRoute>
                }
            >
                <Route index element={<Home />} />
                <Route path="books" element={<Books />} />

                {/* 👇 ВОТ ТУТ теперь настоящий профиль */}
                <Route path="profile" element={<Profile />} />

            </Route>

        </Routes>
    );
}
