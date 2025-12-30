import { useEffect, useState } from 'react'

interface Quote {
    id: number
    author: string
    content: string
    is_featured: boolean
}

export default function Index() {
    const [quotes, setQuotes] = useState<Quote[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetch('/api/quotes/')
            .then(res => {
                if (!res.ok) throw new Error('API ERROR')
                return res.json()
            })
            .then(data => {
                setQuotes(data)
                setLoading(false)
            })
            .catch(err => {
                console.error(err)
                setLoading(false)
            })
    }, [])

    if (loading) return <p className="text-center py-10">Loading...</p>

    return (
        <div className="container mx-auto px-2 min-h-screen">
            <h1 className="text-4xl font-bold">Quotes API</h1>
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                {quotes.map(quote => (
                    <div key={quote.id} className="bg-white rounded-lg shadow p-6">
                        <p className="text-lg italic mb-4">「{quote.content}」</p>
                        <p className="text-right text-gray-600">— {quote.author}</p>
                        {quote.is_featured && <span className="inline-block mt-2 px-3 py-1 bg-yellow-200 text-yellow-800 rounded-full text-sm">Selected</span>}
                    </div>
                ))}
            </div>
        </div>
    )
}