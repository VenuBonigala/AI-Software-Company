import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { EyeIcon, EyeSlashIcon } from "@heroicons/react/24/outline";

const loginSchema = z.object({
  email: z.string().email({ message: "Invalid email address" }),
  password: z
    .string()
    .min(8, { message: "Password must be at least 8 characters" }),
  remember: z.boolean().optional(),
});

export default function LoginPage() {
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [apiError, setApiError] = useState("");
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors, isValid },
  } = useForm({
    resolver: zodResolver(loginSchema),
    mode: "onChange",
    defaultValues: { remember: false },
  });

  // Remember me persistence
  useEffect(() => {
    const saved = localStorage.getItem("rememberMe");
    if (saved === "true") {
      setValue("remember", true);
    }
  }, [setValue]);

  const onSubmit = async (data) => {
    setApiError("");
    setLoading(true);
    try {
      // Mock API call
      await new Promise((res) => setTimeout(res, 1500));
      // On success, redirect placeholder
      console.log("Logged in", data);
    } catch (e) {
      setApiError("Login failed. Please check your credentials.");
    } finally {
      setLoading(false);
    }

    // Store remember flag
    if (data.remember) {
      localStorage.setItem("rememberMe", "true");
    } else {
      localStorage.removeItem("rememberMe");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 to-purple-200 p-4 dark:from-gray-900 dark:to-gray-800">
      <div className="w-full max-w-md bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 space-y-6">
        <h2 className="text-2xl font-bold text-center text-gray-800 dark:text-gray-100">
          Sign in to your account
        </h2>

        {apiError && (
          <div
            role="alert"
            className="bg-red-100 text-red-800 border border-red-200 rounded-md p-3 text-sm"
          >
            {apiError}
          </div>
        )}

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
          {/* Email */}
          <div className="relative">
            <label htmlFor="email" className="sr-only">
              Email address
            </label>
            <input
              id="email"
              type="email"
              placeholder="Email address"
              {...register("email")}
              aria-invalid={errors.email ? "true" : "false"}
              className={`block w-full rounded-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 
                bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:focus:border-indigo-400 
                ${errors.email ? "border-red-500" : ""} 
                py-2.5 px-4 placeholder-gray-500 text-gray-900 dark:text-gray-100`}
            />
            {errors.email && (
              <p className="mt-1 text-sm text-red-600" role="alert">
                {errors.email.message}
              </p>
            )}
          </div>

          {/* Password */}
          <div className="relative">
            <label htmlFor="password" className="sr-only">
              Password
            </label>
            <input
              id="password"
              type={showPassword ? "text" : "password"}
              placeholder="Password"
              {...register("password")}
              aria-invalid={errors.password ? "true" : "false"}
              className={`block w-full rounded-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 
                bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:focus:border-indigo-400 
                ${errors.password ? "border-red-500" : ""} 
                py-2.5 px-4 placeholder-gray-500 text-gray-900 dark:text-gray-100`}
            />
            <button
              type="button"
              onClick={() => setShowPassword((p) => !p)}
              aria-label={showPassword ? "Hide password" : "Show password"}
              className="absolute inset-y-0 right-3 flex items-center text-gray-500 hover:text-gray-700"
            >
              {showPassword ? (
                <EyeSlashIcon className="h-5 w-5" />
              ) : (
                <EyeIcon className="h-5 w-5" />
              )}
            </button>
            {errors.password && (
              <p className="mt-1 text-sm text-red-600" role="alert">
                {errors.password.message}
              </p>
            )}
          </div>

          {/* Remember & Forgot */}
          <div className="flex items-center justify-between">
            <label className="inline-flex items-center">
              <input
                type="checkbox"
                {...register("remember")}
                className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
              />
              <span className="ml-2 text-sm text-gray-600 dark:text-gray-300">
                Remember me
              </span>
            </label>
            <a
              href="#"
              className="text-sm text-indigo-600 hover:underline dark:text-indigo-400"
            >
              Forgot password?
            </a>
          </div>

          {/* Submit */}
          <div>
            <button
              type="submit"
              disabled={!isValid || loading}
              className={`w-full flex justify-center items-center rounded-md px-4 py-2.5 text-sm font-medium 
                text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 
                disabled:opacity-50 disabled:cursor-not-allowed transition-colors`}
            >
              {loading && (
                <svg
                  className="animate-spin -ml-1 mr-2 h-5 w-5 text-white"
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
                    d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 00-8 8h4z"
                  ></path>
                </svg>
              )}
              Sign In
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}