import os
import hashlib
from typing import Optional, Tuple

def save_uploaded_file_securely(
    file_content: bytes, 
    original_filename: str, 
    upload_dir: str, 
    allowed_extensions: set = {'pdf', 'png', 'jpg', 'txt'}
) -> Tuple[bool, str]:
    """
    HIVE STANDARD: Secure File Saver.
    1. Генерирует уникальное имя (SHA256).
    2. Проверяет расширение.
    3. Предотвращает Path Traversal атаки.
    """
    
    # 1. Проверка расширения
    ext = original_filename.split('.')[-1].lower()
    if ext not in allowed_extensions:
        return False, f"Error: Extension .{ext} is not allowed."

    # 2. Генерация безопасного имени (Хеш от контента)
    file_hash = hashlib.sha256(file_content).hexdigest()
    safe_filename = f"{file_hash}.{ext}"
    
    # 3. Полный путь
    full_path = os.path.join(upload_dir, safe_filename)
    
    # 4. Запись (с созданием папки)
    try:
        os.makedirs(upload_dir, exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(file_content)
        return True, full_path
    except Exception as e:
        return False, str(e)
