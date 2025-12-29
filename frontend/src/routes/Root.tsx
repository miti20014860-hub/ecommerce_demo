import { Outlet } from 'react-router-dom'
import Navbar from '../components/Navbar'

export default function Root() {
    return (
        <>
            <main className="min-h-screen">
                <Navbar />

                <div className="px-2 pt-2">

                    <Outlet />  {/* The content of the sub-route will be rendered here. */}
                </div>
            </main>
        </>
    )
}