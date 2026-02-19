import { Outlet } from 'react-router-dom'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'

export const Root = () => {
  return (
    <main className='min-h-screen'>
      <Navbar />
      <Outlet />
      <Footer />
    </main>
  )
}

export default Root
