import React from 'react'
import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import 'leaflet/dist/leaflet.css';
import '@/main.css'

import Root from '@/routes/Root'
import Index from '@/routes/Index/Index'
import News from '@/routes/Index/News'
import Notice from '@/routes/Index/Notice'
import Activity from '@/routes/acitivity/Activity'
import Collection from '@/routes/Collection'
import Kenshi from '@/routes/Kenshi'
import Member from '@/routes/Member'
import ErrorPage from '@/routes/ErrorPage'
import About from '@/routes/footer/About'
import Contact from '@/routes/footer/Contact'
import FAQ from '@/routes/footer/FAQ'
import Privacy from '@/routes/footer/Privacy'
import Terms from '@/routes/footer/Terms'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <Index />, },
      { path: 'news/:id', element: <News />, },
      { path: 'notice/:id', element: <Notice />, },
      { path: 'activity/*', element: <Activity />, },
      { path: 'collection/*', element: <Collection />, },
      { path: 'kenshi/*', element: <Kenshi />, },
      { path: 'member/*', element: <Member />, },
      { path: 'about/*', element: <About />, },
      { path: 'contact/*', element: <Contact />, },
      { path: 'faq/*', element: <FAQ />, },
      { path: 'privacy/*', element: <Privacy />, },
      { path: 'terms/*', element: <Terms />, },
    ],
  },
])

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5,
      retry: 1,
    },
  },
})

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </React.StrictMode>,
)