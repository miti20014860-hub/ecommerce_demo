import React from 'react'
import ReactDOM from 'react-dom/client'
import { AuthProvider } from '@/components/partials/AuthProvider';
import { ProtectedRoute } from '@/components/partials/ProtectedRoute';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import 'leaflet/dist/leaflet.css';
import '@/main.css'

import Root from '@/routes/Root'
import Index from '@/routes/index/Index'
import News from '@/routes/index/News'
import Notice from '@/routes/index/Notice'
import Activity from '@/routes/activity/Activity'
import ActivityDetail from '@/routes/activity/ActivityDetail'
import Collection from '@/routes/collection/Collection'
import CollectionDetail from '@/routes/collection/CollectionDetail'
import Kenshi from '@/routes/kenshi/Kenshi'
import Member from '@/routes/member/Member'
import Account from '@/routes/member/Account'
import About from '@/routes/footer/About'
import Contact from '@/routes/footer/Contact'
import FAQ from '@/routes/footer/FAQ'
import Privacy from '@/routes/footer/Privacy'
import Terms from '@/routes/footer/Terms'
import ErrorPage from '@/routes/ErrorPage'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <Index /> },
      { path: 'news/:id', element: <News /> },
      { path: 'notice/:id', element: <Notice /> },
      { path: 'activity/:id', element: <ActivityDetail /> },
      { path: 'activity/*', element: <Activity /> },
      { path: 'collection/:id', element: <CollectionDetail /> },
      { path: 'collection/*', element: <Collection /> },
      { path: 'kenshi/*', element: <Kenshi /> },
      { path: 'member/account/*', element: <ProtectedRoute><Account /></ProtectedRoute> },
      { path: 'member/*', element: <Member /> },
      { path: 'about/*', element: <About /> },
      { path: 'contact/*', element: <Contact /> },
      { path: 'faq/*', element: <FAQ /> },
      { path: 'privacy/*', element: <Privacy /> },
      { path: 'terms/*', element: <Terms /> }
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
      <AuthProvider>
        <RouterProvider router={router} />
      </AuthProvider>
    </QueryClientProvider>
  </React.StrictMode>,
)