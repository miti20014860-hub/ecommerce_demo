from django.core.management import call_command
from django.core import serializers
import subprocess
import django
import sys
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

EXPORT_MODELS = [
    'activity.Activity',
    'activity.ActivityImage',
    'collection.Collection',
    'collection.CollectionImage',
    'index.Banner',
    'index.Quote',
    'index.News',
    'index.NewsImage',
    'index.Notice',
    'index.NoticeImage',
    'kenshi.Kenshi',
    'kenshi.KenshiImage',
    'others.About',
    'others.Contact',
    'others.Terms',
    'others.Part',
    'others.Section',
    'others.Privacy',
    'others.Faq',
    'member.CustomUser',
]


OUTPUT_DIR = os.path.join(BASE_DIR, 'export_data')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_to_json():
    for model_path in EXPORT_MODELS:
        app_label, model_name = model_path.split('.')
        try:
            Model = django.apps.apps.get_model(app_label, model_name)
        except LookupError:
            print(f"[!] Model not found: {model_path}")
            continue

        queryset = Model.objects.all()
        count = queryset.count()
        if count == 0:
            print(f"[i] {model_path} No information available, skipped.")
            continue

        filename = f"{app_label}_{model_name.lower()}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            serializers.serialize('json', queryset, stream=f, indent=2, ensure_ascii=False)

        print(f"[Success] {model_path} → {filename} ({count} record{'s' if count != 1 else ''})")


def clean_data():
    print("\nCleaning data from specified models...")
    deleted_total = 0

    for model_path in EXPORT_MODELS:
        app_label, model_name = model_path.split('.')
        try:
            Model = django.apps.apps.get_model(app_label, model_name)
        except LookupError:
            print(f"[!] Model not found: {model_path}")
            continue

        count = Model.objects.count()
        if count == 0:
            print(f"[i] {model_path}: No data to delete.")
            continue

        Model.objects.all().delete()
        print(f"[Success] Deleted {count} record{'s' if count != 1 else ''} from {model_path}")
        deleted_total += count

    print(f"\n[Summary] Clean completed! Total {deleted_total} record(s) deleted.")


def import_from_json():
    if not os.path.exists(OUTPUT_DIR):
        print(f"[Error] Export directory not found: {OUTPUT_DIR}")
        return

    json_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.json')]
    if not json_files:
        print(f"[i] No JSON files found in {OUTPUT_DIR}")
        return

    print(f"[i] Found {len(json_files)} JSON file(s) to import:")
    for f in json_files:
        print(f"   • {f}")

    if not confirm("Run: python manage.py loaddata export_data/*.json ?", default=False):
        print("Import cancelled.")
        return

    print(f"\nRunning: python manage.py loaddata {OUTPUT_DIR}/*.json")
    try:
        result = subprocess.run(
            ['python', 'manage.py', 'loaddata'] + [os.path.join(OUTPUT_DIR, f) for f in json_files],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print("[Success] All data imported successfully via manage.py loaddata!")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Import failed:\n{e.stderr}")


def confirm(prompt, default=False):
    while True:
        choice = input(f"{prompt} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        elif choice == '':
            return default
        else:
            print("y/n")


def main_menu():
    print("\n" + "="*50)
    print("    Django Data Export Tool")
    print("="*50)

    # Option 1: Export data
    if confirm("Do you want to export data?", default=True):
        export_to_json()
    else:
        print("Data export cancelled.")

    # Option 2: Clean data
    if confirm("Do you want to CLEAN data (delete only app data)?", default=False):
        if confirm("WARNING: This will delete ALL data in your models! Continue?", default=False):
            clean_data()
        else:
            print("Clean cancelled.")
    else:
        print("Skipping data cleaning.")

    # Option 3: Format database
    if confirm("Do you want to format the database (delete all data)?", default=False):
        if confirm("WARNING: This will delete ALL data! Are you sure you want to continue?", default=False):
            print("Formatting database...")
            call_command('flush', '--no-input')
            print("[Success] Database has been formatted (all data cleared).")
        else:
            print("Database formatting cancelled.")
    else:
        print("Skipping database formatting.")

    # Option 4: Import data
    if confirm("Do you want to import data from JSON files?", default=False):
        import_from_json()
    else:
        print("Data import skipped.")


if __name__ == '__main__':
    main_menu()
