import { Link, useLocation } from 'react-router-dom';

export default function Footer() {

  const location = useLocation();
  const pathname = location.pathname;
  const isCurrent = (path: string) => {
    return pathname.startsWith(path);
  };

  return (
    <footer className='bg-gray-100 border-y-1 text-sm mt-5'>
      <div className='container mx-auto lg:px-8 xl:px-16 2xl:px-24 my-6'>
        {/* Link */}
        <div className='nav-link text-center md:text-right my-4'>
          <Link to='/about/'
            className='mx-2 sm:mx-6'
            aria-current={isCurrent('/about/') ? 'page' : undefined}>About Us |</Link>
          <Link to='/contact/'
            className='mx-2 sm:mx-6'
            aria-current={isCurrent('/contact/') ? 'page' : undefined}>Contact |</Link>
          <Link to='/faq/'
            className='mx-2 sm:mx-6'
            aria-current={isCurrent('/faq/') ? 'page' : undefined}>FAQ |</Link>
          <Link to='/privacy/'
            className='mx-2 sm:mx-6'
            aria-current={isCurrent('/privacy/') ? 'page' : undefined}>Privacy |</Link>
          <Link to='/terms/'
            className='mx-2 sm:mx-6'
            aria-current={isCurrent('/terms/') ? 'page' : undefined}>Terms & Conditions |</Link>
        </div >
        {/* Copyright */}
        <p className='text-center md:text-left lg:ms-4' >© Habaki, Ltd. All Rights Reserved.</p>
      </div >
    </footer >
  );
};