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

// 匯入你的 CSS（Tailwind v4 已設定）
import './main.css'  // 或 './index.css'，看你檔名

// 匯入路由頁面（建議放在 src/routes/ 資料夾）
import Root from './routes/Root'              // 主布局（包含 Navbar、Footer 等）
import Index from './routes/Index'              // 首頁（News）
import Activity from './routes/Activity'
import Collection from './routes/Collection'
import Kenshi from './routes/Kenshi'
import Member from './routes/Member'
import ErrorPage from './routes/ErrorPage'      // 404 或錯誤頁

// 建立路由器
const router = createBrowserRouter([
  {
    path: "/",                  // 根路徑
    element: <Root />,          // 所有頁面共用的布局（Navbar + Outlet + Footer）
    errorElement: <ErrorPage />, // 任何路由錯誤時顯示
    children: [                 // 子路由（內容會渲染在 Root 的 <Outlet /> 位置）
      {
        index: true,            // 對應 / （首頁）
        element: <Index />,
      },
      {
        path: "activity/*",     // /activity/ 及子頁面
        element: <Activity />,
      },
      {
        path: "collection/*",
        element: <Collection />,
      },
      {
        path: "kenshi/*",
        element: <Kenshi />,
      },
      {
        path: "member/*",       // 包含登入後的 /member/account/ 等
        element: <Member />,
      },
    ],
  },
])

// 渲染
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)