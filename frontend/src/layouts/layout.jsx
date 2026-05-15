import { Outlet, Link, useNavigate } from "react-router-dom";
import "./layout.css";

export default function Layout() {
    const navigate = useNavigate();

    function logout() {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        navigate("/login");
    }

    return (
        <div className="app-layout">

            {/* NAVBAR */}
            <nav className="navbar">
                <div className="navbar-inner">

                    <Link className="logo" to="/">
                        <img src="/logo.svg" alt="Libro" className="logo-icon" />
                            Libro
                    </Link>

                    <div className="nav-links">

                        <Link className="nav-btn" to="/">
                            Главная
                        </Link>

                        <Link className="nav-btn" to="/libraries">
                            Библиотеки
                        </Link>

                        <Link className="nav-btn" to="/books">
                            Книги
                        </Link>

                        <Link className="nav-btn" to="/profile">
                            Профиль
                        </Link>

                        <button onClick={logout} className="logout-btn">
                            Выйти
                        </button>

                    </div>

                </div>
            </nav>

            {/* CONTENT */}
            <div className="page-content">
                <div className="container">
                    <Outlet />
                </div>
            </div>

        </div>
    );
}