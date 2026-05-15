import { Routes, Route, Navigate } from "react-router-dom";

import Layout from "./layouts/Layout";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import EditProfile from "./pages/EditProfile";
import Books from "./pages/Books";
import BookDetail from "./pages/BookDetail";
import Libraries from "./pages/Libraries";
import LibraryDetail from "./pages/LibraryDetail";

function Home() {
    return <h1>Главная</h1>;
}



function PrivateRoute({ children }) {
    const token = localStorage.getItem("access");
    return token ? children : <Navigate to="/login" />;
}

export default function App() {
    return (
        <Routes>

            {/* LOGIN */}
            <Route path="/login" element={<Login />} />

            {/* PROTECTED AREA */}
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
                <Route path="books/:id" element={<BookDetail />} />

                {/* PROFILE */}
                <Route path="profile" element={<Profile />} />

                {/* EDIT PROFILE (🔥 ВОТ ЭТО ТЫ ЗАБЫЛА) */}
                <Route path="profile/edit" element={<EditProfile />} />

                <Route path="libraries" element={<Libraries />} />
                <Route path="libraries/:id" element={<LibraryDetail />} />

            </Route>

        </Routes>
    );
}