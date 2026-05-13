import { useForm } from "react-hook-form";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function LoginPage() 
  const {
    register,
    handleSubmit,
    formState: { errors, isValid, isSubmitting },
  } = useForm({ mode: "onChange" });
  const navigate = useNavigate();
  const [apiError, setApiError] = useState("");

  const onSubmit = async (data) => {
    setApiError("");
    try {
      // Mock API call – replace with real endpoint
      await new Promise((res, rej) =>
        setTimeout(() => {
          data.email === "demo@example.com" && data.password === "demo123"
            ? res()
            : rej(new Error("Invalid credentials"));
        }, 1500),
      );
      navigate("/dashboard");
    } catch (err) {
      setApiError(err.message);
    }
  };

  return (
    <div className="relative flex min-h-screen items-center justify-center bg-gradient-to-br from-indigo-100 to-indigo-300 dark:from-gray-900 dark:to-gray-800 p-4">
      {/* Card */}
      <div className="w-full max-w-md space-y-6 rounded-xl bg-white p-8 shadow-lg dark:bg-gray-800 dark:shadow-none">
        <h2 className="text-center text-2xl font-bold text-gray-800 dark:text-gray-100">
          Sign in to your account
        </h2>

        {/* API error */}
        {apiError && (
          <div
            role="alert"
            className="rounded border border-red-200 bg-red-50 p-2 text-sm text-red-600"
          >
            {apiError}
          </div>
        )}

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {/* Email */}
          <div>
            <label
              htmlFor="email"
              className="block text-sm font-medium text-gray-700 dark:text-gray-200"
            >
              Email address
            </label>
            <input
              id="email"
              type="email"
              className={`
                mt-1 block w-full rounded-md border
                ${errors.email ? "border-red-500" : "border-gray-300"}
                bg-white py-2 px-3 shadow-sm placeholder-gray-400 focus:border-indigo-500
                focus:outline-none focus:ring-indigo-500 sm:text-sm
                dark:bg-gray-700 dark:text-gray-100 dark:placeholder-gray-400
              `}
              placeholder="you@example.com"
              {...register("email", {
                required: "Email is required",
                pattern: {
                  value: /^\S+@\S+$/i,
                  message: "Enter a valid email",
                },
              })}
            />
            {errors.email && (
              <p className="mt-1 text-xs text-red-600" role="alert">
                {errors.email.message}
              </p>
            )}
          </div>

          {/* Password */}
          <div>
            <label
              htmlFor="password"
              className="block text-sm font-medium text-gray-700 dark:text-gray-200"
            >
              Password
            </label>
            <input
              id="password"
              type="password"
              className={`
                mt-1 block w-full rounded-md border
                ${errors.password ? "border-red-500" : "border-gray-300"}
                bg-white py-2 px-3 shadow-sm placeholder-gray-400 focus:border-indigo-500
                focus:outline-none focus:ring-indigo-500 sm:text-sm
                dark:bg-gray-700 dark:text-gray-100 dark:placeholder-gray-400
              `}
              placeholder="••••••••"
              {...register("password", {
                required: "Password is required",
                minLength: {
                  value: 6,
                  message: "Password must be at least 6 characters",
                },
              })}
            />
            {errors.password && (
              <p className="mt-1 text-xs text-red-600" role="alert">
                {errors.password.message}
              </p>
            )}
          </div>

          {/* Remember + Forgot */}
          <div className="flex items-center justify-between">
            <label className="inline-flex items-center">
              <input
                type="checkbox"
                className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                {...register("remember")}
              />
              <span className="ml-2 text-sm text-gray-600 dark:text-gray-300">
                Remember me
              </span>
            </label>
            <a
              href="#"
              className="text-sm font-medium text-indigo-600 hover:underline dark:text-indigo-400"
            >
              Forgot password?
            </a>
          </div>

          {/* Submit */}
          <div>
            <button
              type="submit"
              disabled={!isValid || isSubmitting}
              className={`
                flex w-full justify-center rounded-md border border-transparent 
                bg-indigo-600 px-4 py-2 text-sm font-medium text-white 
                hover:bg-indigo-700 focus:outline-none focus:ring-2 
                focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50
                ${isSubmitting && "relative"}
              `}
            >
              {isSubmitting && (
                <svg
                  className="absolute left-3 h-5 w-5 animate-spin text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  ></circle>
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 00-8 8h4l-3 3 3-3H4z"
                  ></path>
                </svg>
              )}
              Sign In
            </button>
          </div>

          {/* Social login placeholders */}
          <div className="mt-6 grid grid-cols-2 gap-3">
            <button
              type="button"
              className="flex items-center justify-center rounded-md border border-gray-300 bg-white py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 dark:bg-gray-700 dark:text-gray-200 dark:border-gray-600"
            >
              {/* Icon placeholder */}
              <svg
                className="mr-2 h-5 w-5"
                viewBox="0 0 24 24"
                fill="currentColor"
              >
                <path d="M12 2C6.48 2 2 6.48 2 12c0 4.84 3.6 8.85 8.3 9.77v-6.91H8.1v-2.86h2.2V9.41c0-2.18 1.3-3.38 3.27-3.38.95 0 1.86.07 2.11.1v2.44h-1.45c-1.14 0-1.36.54-1.36 1.33v1.75h2.73l-.36 2.86h-2.37v6.91C18.4 20.85 22 16.84 22 12c0-5.52-4.48-10-10-10z" />
              </svg>
              Google
            </button>
            <button
              type="button"
              className="flex items-center justify-center rounded-md border border-gray-300 bg-white py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 dark:bg-gray-700 dark:text-gray-200 dark:border-gray-600"
            >
              <svg
                className="mr-2 h-5 w-5"
                viewBox="0 0 24 24"
                fill="currentColor"
              >
                <path d="M12 0C5.371 0 0 5.371 0 12c0 5.302 3.438 9.8 8.206 11.385v-8.05H5.897V12h2.309V9.797c0-2.285 1.373-3.544 3.492-3.544.99 0 1.874.073 2.126.107v2.468h-1.459c-1.144 0-1.366.545-1.366 1.347V12h2.733l-.356 3.335h-2.377v8.05C20.562 21.8 24 17.302 24 12c0-6.629-5.371-12-12-12z" />
              </svg>
              GitHub
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
