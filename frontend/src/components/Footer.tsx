import { Link } from 'react-router-dom';

const Footer = () => {

   return (
      <footer className="border-y-2 bg-gray-100">
         <div className="container mx-auto my-5">
            {/* Link */}
            <div className="nav-link my-7 text-end">
               <Link to="/about/"
                  className="mx-3">About Us |</Link>
               <Link to="/contact/"
                  className="mx-3">Contact |</Link>
               <Link to="/terms/"
                  className="mx-3">Terms & Conditions |</Link>
               <Link to="/privacy/"
                  className="mx-3">Privacy |</Link>
               <Link to="/faq/"
                  className="mx-3">FAQ |</Link>
            </div >
            {/* Copyright */}
            < div className="ms-3" >
               <small>© Habaki, Ltd. All Rights Reserved.</small>
            </div >
         </div >
      </footer >
   );
};

export default Footer;