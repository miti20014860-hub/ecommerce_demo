import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { signIn, signUp } from '@/lib/fetcher';
import type { AuthResponse, RegisterResponse, SignIn, SignUp } from '@/types/type';

export const Menber = () => {
  const [isSignUpOpen, setIsSignUpOpen] = useState(false);

  const [signInData, setSignInData] = useState({
    username: '',
    password: ''
  });

  const [signUpData, setSignUpData] = useState({
    username: '',
    email: '',
    password1: '',
    password2: ''
  });

  const signInMutation = useMutation<AuthResponse, Error, SignIn>({
    mutationFn: signIn,
    onSuccess: (data) => {
      console.log('Login Success', data.access);
      window.location.href = '/member/account/';
    },
    onError: (error) => { alert(error.message); }
  });

  const signUpMutation = useMutation<RegisterResponse, Error, SignUp>({
    mutationFn: signUp,
    onSuccess: (data) => {
      console.log('Registration Success', data.username);
      alert('Registration successful! Please sign in.');
      setIsSignUpOpen(false);
    },
    onError: (error) => {
      try {
        const fieldErrors = JSON.parse(error.message);
        console.log('Fields with errors:', fieldErrors);
        alert('Registration failed. Please check the fields.');
      } catch {
        alert(error.message);
      }
    },
  });

  return (
    <div className="flex items-center justify-center py-12 px-4">
      <div className="max-w-md w-full bg-white border border-slate-500 p-8 shadow-sm">

        {/* Sign In Header */}
        <div className="mb-7">
          <h2 className="text-3xl font-medium mb-3">Sign in</h2>
        </div>

        {/* Sign In Form */}
        <form onSubmit={(e) => { e.preventDefault(); signInMutation.mutate(signInData); }} className="space-y-4">
          <div className="relative border-2 rounded-md border-slate-200 focus-within:border-black transition-colors">
            <input
              required
              type="text"
              placeholder="Username"
              onChange={(e) => setSignInData({ ...signInData, username: e.target.value })}
              className="w-full pb-2 pt-6 px-2 outline-none text-md placeholder-transparent peer"
            />
            <label className="absolute left-0 top-4 px-2 text-sm text-slate-500 transition-all peer-focus:top-1 peer-not-placeholder-shown:top-1">
              Username
            </label>
          </div>
          <div className="relative border-2 rounded-md border-slate-200 focus-within:border-black transition-colors">

            <input
              required
              type="password"
              placeholder="Password"
              onChange={(e) => setSignInData({ ...signInData, password: e.target.value })}
              className="w-full pb-2 pt-6 px-2 outline-none text-md placeholder-transparent peer"
            />
            <label className="absolute left-0 top-4 px-2 text-sm text-slate-500 transition-all peer-focus:top-1 peer-not-placeholder-shown:top-1">
              Password
            </label>
          </div>

          <button
            type="submit"
            className="w-full text-lg bg-black text-white py-3 font-medium hover:bg-slate-800 transition-colors"
          >
            SING IN
          </button>
        </form>

        {/* Registration Section */}
        <div className="mt-12">
          <h2 className="text-[28px] font-medium">Not a member?</h2>

          <button
            onClick={() => setIsSignUpOpen(!isSignUpOpen)}
            className={`w-full text-lg py-3 mt-3 font-medium border border-black transition-all ${isSignUpOpen ? 'bg-white text-black' : 'bg-slate-500 text-white hover:bg-slate-600'
              }`}
          >
            SIGN UP
          </button>

          {/* Animated Collapse Container */}
          <div className={`overflow-hidden transition-all duration-300 ${isSignUpOpen ? 'max-h-[600px] mt-6' : 'max-h-0'}`}>
            <h3 className="mb-4 text-lg text-red-700 font-medium uppercase tracking-tight">Required Fields</h3>

            <form onSubmit={(e) => { e.preventDefault(); signUpMutation.mutate(signUpData); }} className="space-y-4">

              <div className="relative border-2 rounded-md border-slate-200 focus-within:border-black transition-colors">
                <input
                  required
                  type="text"
                  placeholder="Username"
                  onChange={(e) => setSignUpData({ ...signUpData, username: e.target.value })}
                  className="w-full pb-2 pt-6 px-2 outline-none text-md placeholder-transparent peer"
                />
                <label className="absolute left-0 top-4 px-2 text-sm text-slate-500 transition-all peer-focus:top-1 peer-not-placeholder-shown:top-1">
                  Username
                </label>
              </div>

              <div className="relative border-2 rounded-md border-slate-200 focus-within:border-black transition-colors">
                <input
                  required
                  type="email"
                  placeholder="Email"
                  onChange={(e) => setSignUpData({ ...signUpData, email: e.target.value })}
                  className="w-full pb-2 pt-6 px-2 outline-none text-md placeholder-transparent peer"
                />
                <label className="absolute left-0 top-4 px-2 text-sm text-slate-500 transition-all peer-focus:top-1 peer-not-placeholder-shown:top-1">
                  Email
                </label>
              </div>

              <div className="relative border-2 rounded-md border-slate-200 focus-within:border-black transition-colors">
                <input
                  required
                  type="password"
                  placeholder="Create a Password"
                  onChange={(e) => setSignUpData({ ...signUpData, password1: e.target.value })}
                  className="w-full pb-2 pt-6 px-2 outline-none text-md placeholder-transparent peer"
                />
                <label className="absolute left-0 top-4 px-2 text-sm text-slate-500 transition-all peer-focus:top-1 peer-not-placeholder-shown:top-1">
                  Create a Password
                </label>
              </div>

              <div className="relative border-2 rounded-md border-slate-200 focus-within:border-black transition-colors">
                <input
                  required
                  type="password"
                  placeholder="Confirm Password"
                  onChange={(e) => setSignUpData({ ...signUpData, password2: e.target.value })}
                  className="w-full pb-2 pt-6 px-2 outline-none text-md placeholder-transparent peer"
                />
                <label className="absolute left-0 top-4 px-2 text-sm text-slate-500 transition-all peer-focus:top-1 peer-not-placeholder-shown:top-1">
                  Confirm Password
                </label>
              </div>

              <button
                type="submit"
                className="w-full text-lg bg-red-600 text-white py-3 font-medium hover:bg-red-700 transition-colors"
              >
                SUBMIT
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Menber
