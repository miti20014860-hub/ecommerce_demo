// import { StrictMode } from 'react'
// import { createRoot } from 'react-dom/client'
// import './main.css'

// import App from './App.tsx'

// createRoot(document.getElementById('root')!).render(
//   <StrictMode>
//     <App />
//   </StrictMode>,
// )
// src/main.tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router-dom'

import './main.css'

import Root from './routes/Root'
import Index from './routes/Index'
import Activity from './routes/Activity'
import Collection from './routes/Collection'
import Kenshi from './routes/Kenshi'
import Member from './routes/Member'
import ErrorPage from './routes/ErrorPage'
import About from './routes/footer/About'
import Contact from './routes/footer/Contact'
import FAQ from './routes/footer/FAQ'
import Privacy from './routes/footer/Privacy'
import Terms from './routes/footer/Terms'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <Index />, },
      { path: "activity/*", element: <Activity />, },
      { path: "collection/*", element: <Collection />, },
      { path: "kenshi/*", element: <Kenshi />, },
      { path: "member/*", element: <Member />, },
      { path: "about/*", element: <About />, },
      { path: "contact/*", element: <Contact />, },
      { path: "faq/*", element: <FAQ />, },
      { path: "privacy/*", element: <Privacy />, },
      { path: "terms/*", element: <Terms />, },
    ],
  },
])

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)