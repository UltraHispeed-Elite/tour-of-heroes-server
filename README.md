## Running

```bash
gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 'heroes_service:create_app()'
```