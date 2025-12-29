interface CurrentUser {
    isAuthenticated: boolean;
    username: string;
}

declare global {
    interface Window {
        currentUser?: CurrentUser;
        csrfToken?: string;
    }
}

export { };