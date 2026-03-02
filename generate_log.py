import requests
import pandas as pd
from datetime import datetime
from rich.console import Console

# Initialize rich console for fancy terminal output
console = Console()

def fetch_post_data(post_id=1):
    """Fetches a post from a placeholder API."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching data:[/bold red] {e}")
        return None

def save_to_csv(data):
    """Saves dictionary data to a timestamped CSV file."""
    if not data:
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"api_data_{timestamp}.csv"
    
    # Convert dict to DataFrame and export
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)
    return filename

def main():
    console.print("[bold cyan]Starting automation script...[/bold cyan]")
    
    # 1. Fetch Data
    post = fetch_post_data()
    
    if post:
        console.print(f"Fetched Post: [green]{post.get('title')}[/green]")
        
        # 2. Save Data
        filename = save_to_csv(post)
        console.print(f"[bold white]Success![/bold white] Data saved to [underline]{filename}[/underline]")
    else:
        console.print("[yellow]No data was saved due to a fetch error.[/yellow]")

if __name__ == "__main__":
    main()