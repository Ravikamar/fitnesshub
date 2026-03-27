# FitnessHub Project Context

This file provides a map of the project structure and key configurations to ensure efficient navigation and consistency.

## Project Structure
- `fitnesshub_project/`: Core project settings and main URL configuration.
- `gym/`: App handling memberships, user profiles, and the landing page.
- `shop/`: App handling product listings and orders.
- `static/`: Global static assets (CSS, JS, Images).
- `templates/`: Global templates, including `base.html`.
- `media/`: User-uploaded content (e.g., product images).

## Key URLs
- Home: `/` (name: `home`)
- Membership Plans: `/memberships/` (name: `membership_plans`)
- Profile: `/profile/` (name: `profile`)
- Shop: `/shop/` (name: `shop_home`)
- Auth: `/login/`, `/logout/`, `/register/`

## Configuration Notes
- `LOGIN_REDIRECT_URL`: Set to `'profile'` to avoid 404 at `/accounts/profile/`.
- `LOGOUT_REDIRECT_URL`: Set to `'home'`.
- `ALLOWED_HOSTS`: Includes `ravikumargaur.pythonanywhere.com` for deployment.

## Common Workflows
- When adding features, ensure templates extend `base.html`.
- Use Bootstrap 5 and custom styles in `static/css/style.css`.
- Verification should include checking URL resolution and authentication state.
