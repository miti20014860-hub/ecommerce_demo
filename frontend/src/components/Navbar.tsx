import { Link, useLocation } from 'react-router-dom';
import { useAuth } from '@/lib/auth-context';

export const Navbar = () => {
  const location = useLocation();
  const pathname = location.pathname;
  const isCurrent = (path: string) => pathname.startsWith(path);
  const { isAuthenticated, isLoading } = useAuth()
  const memberHref = !isLoading && isAuthenticated ? '/member/account' : '/member';

  return (
    <nav className='container mx-auto 2xl:px-24 font-serif'>
      {/* Logo */}
      <header className='nav-link border-b-1 text-center p-2'>
        <Link to='/'
          className='text-3xl'
          aria-current={pathname === '/' ? 'page' : undefined}>Habaki</Link>
      </header>

      {/* Link */}
      <div className='nav-link border-b-1 text-lg p-1 mb-1'>
        <div className='flex justify-between px-2 py-1'>
          <Link to='/'
            className={`px-2 ${pathname === '/' || isCurrent('/news/') || isCurrent('/notice/') ? 'border-b-2' : 'hover:border-b-2'}`}
            aria-current={pathname === '/' || isCurrent('/news/') || isCurrent('/notice/') ? 'page' : undefined}>News</Link>
          <Link to='/activity/'
            className={`px-2 ${isCurrent('/activity/') ? 'border-b-2' : 'hover:border-b-2'}`}
            aria-current={isCurrent('/activity/') ? 'page' : undefined}>Activity</Link>
          <Link to='/collection/'
            className={`px-2 ${isCurrent('/collection/') ? 'border-b-2' : 'hover:border-b-2'}`}
            aria-current={isCurrent('/collection/') ? 'page' : undefined}>Collection</Link>
          <Link to='/kenshi/'
            className={`px-2 ${isCurrent('/kenshi/') ? 'border-b-2' : 'hover:border-b-2'}`}
            aria-current={isCurrent('/kenshi/') ? 'page' : undefined}>Kenshi</Link>
          <Link to={memberHref}
            className={`px-2 ${isCurrent('/member') ? 'border-b-2' : 'hover:border-b-2'}`}
            aria-current={isCurrent('/member') ? 'page' : undefined}>Member</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar