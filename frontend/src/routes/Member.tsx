import { Outlet } from 'react-router-dom'

export default function Member() {
    return (
        <>
            <main className="min-h-screen">
                <Outlet />  {/* The content of the sub-route will be rendered here. */}
            </main>
        </>
    )
}