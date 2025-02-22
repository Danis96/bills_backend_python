import sys
import subprocess
from typing import Optional

def run_migration(commit_message: Optional[str] = None) -> None:
    """
    Run database migrations using Alembic
    
    Args:
        commit_message (str, optional): Message for the migration commit
    """
    try:
        # 1. Upgrade to current head first
        print("Applying existing migrations...")
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        
        if commit_message:
            # 2. Create new migration
            print(f"\nCreating new migration: {commit_message}")
            subprocess.run(["alembic", "revision", "--autogenerate", "-m", commit_message], check=True)
            
            # 3. Apply new migration
            print("\nApplying new migration...")
            subprocess.run(["alembic", "upgrade", "head"], check=True)
            
        print("\nMigration completed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"\nError during migration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Use provided commit message
        run_migration(sys.argv[1])
    else:
        # Just upgrade to current head
        run_migration() 