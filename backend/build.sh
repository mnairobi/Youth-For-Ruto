#!/usr/bin/env bash
set -o errexit

echo ""
echo "========================================"
echo "  YR27 Backend — Build Starting"
echo "  Youth Power. National Power."
echo "========================================"
echo ""

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "📁 Collecting static files..."
python manage.py collectstatic --no-input --clear

echo ""
echo "🗄️  Running database migrations..."
python manage.py migrate --no-input

echo ""
echo "🌱 Seeding initial data..."
python manage.py seed_data || echo "⚠️  Seed already ran or skipped"

echo ""
echo "========================================"
echo "  ✅ Build Complete!"
echo "  🚀 YR27 Backend Ready"
echo "========================================"
echo ""