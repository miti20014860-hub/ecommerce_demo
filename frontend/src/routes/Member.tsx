import { Outlet } from 'react-router-dom'
import Navbar from '../components/Navbar'

export default function Member() {
    return (
        <>
            <Navbar />
            <main className="min-h-screen">
                <Outlet />  {/* The content of the sub-route will be rendered here. */}
            </main>
        </>
    )
}