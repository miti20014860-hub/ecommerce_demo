import { useRouteError } from 'react-router-dom'

export default function ErrorPage() {
    const error = useRouteError() as any
    console.error(error)

    return (
        <div className="container mx-auto px-4 py-16 text-center">
            <h1 className="text-6xl font-bold text-red-600 mb-4">404</h1>
            <p className="text-xl mb-8">Page does not exist</p>
            <a href="/" className="text-blue-600 hover:underline">Return to homepage</a>
        </div>
    )
}