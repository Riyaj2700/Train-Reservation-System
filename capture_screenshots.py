import os
import time
import re
from playwright.sync_api import sync_playwright

def run():
    print("Starting screenshot capture...")
    screenshot_dir = r"c:\Users\A\OneDrive\Desktop\Train Reservation System\screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})
        
        # 1. Welcome Page
        print("Opening http://localhost:8080...")
        page.goto("http://localhost:8080")
        time.sleep(1)
        # Ensure we are logged out to show welcome screen
        if page.locator("#user-info button").is_visible():
            page.click("#user-info button")
            time.sleep(0.5)
        
        welcome_path = os.path.join(screenshot_dir, "1_welcome.png")
        page.screenshot(path=welcome_path)
        print(f"Saved Welcome screen to {welcome_path}")

        # 2. Login Page
        print("Clicking Login in Navbar...")
        page.click("#auth-buttons button")
        time.sleep(0.5)
        login_path = os.path.join(screenshot_dir, "2_login.png")
        page.screenshot(path=login_path)
        print(f"Saved Login screen to {login_path}")

        # Login
        print("Entering credentials and logging in...")
        page.fill("#username", "user")
        page.fill("#password", "password")
        page.click('button[onclick="login()"]')
        
        # Wait for dashboard to load
        print("Waiting for dashboard...")
        page.wait_for_selector("#dashboard-section", state="visible", timeout=5000)
        time.sleep(0.5)

        # 3. Search Trains
        print("Entering search route...")
        page.fill("#routeSource", "Mumbai")
        page.fill("#routeDest", "Delhi")
        page.click('button[onclick="searchTrainsByRoute()"]')
        
        # Wait for train options to load
        print("Waiting for train search results...")
        page.wait_for_selector("#trainNumber option[value='12951']", state="attached", timeout=5000)
        time.sleep(0.5)

        print("Selecting train...")
        page.select_option("#trainNumber", "12951") # Mumbai Rajdhani Express
        time.sleep(0.5)

        search_results_path = os.path.join(screenshot_dir, "3_search_results.png")
        page.screenshot(path=search_results_path)
        print(f"Saved Search Results screen to {search_results_path}")

        # 4. Booking
        print("Filling booking and passenger details...")
        page.fill("#dateOfJourney", "2026-06-15")
        
        # Fill passenger details
        page.fill(".passenger-row .p-name", "John Doe")
        page.fill(".passenger-row .p-age", "30")
        page.select_option(".passenger-row .p-gender", "Male")
        
        # Fill payment details
        page.fill(".p-card", "1234567890123456")
        page.fill(".p-expiry", "12/28")
        page.fill(".p-cvv", "123")

        print("Clicking Pay & Book Ticket...")
        page.click("#bookBtn")
        
        # Wait for the payment delay and confirmation pass
        print("Waiting for booking result...")
        page.wait_for_selector("#booking-result", state="visible", timeout=6000)
        time.sleep(0.5)

        boarding_pass_path = os.path.join(screenshot_dir, "4_boarding_pass.png")
        page.screenshot(path=boarding_pass_path)
        print(f"Saved Boarding Pass screen to {boarding_pass_path}")

        # Extract PNR
        booking_result_text = page.locator("#booking-result").inner_text()
        print("Booking Result text read successfully.")
        pnr_match = re.search(r"PNR:\s*([A-Z0-9]+)", booking_result_text)
        if not pnr_match:
            print("Failed to find PNR number in booking result!")
            browser.close()
            return
        
        pnr = pnr_match.group(1)
        print(f"Extracted PNR: {pnr}")

        # 5. View Ticket Tab
        print("Navigating to View Ticket tab...")
        page.click("#view-tab")
        page.wait_for_selector("#viewPnr", state="visible")
        page.fill("#viewPnr", pnr)
        page.click('button[onclick="viewTicket()"]')
        page.wait_for_selector("#view-details", state="visible", timeout=5000)
        time.sleep(0.5)

        view_ticket_path = os.path.join(screenshot_dir, "5_view_ticket.png")
        page.screenshot(path=view_ticket_path)
        print(f"Saved View Ticket screen to {view_ticket_path}")

        # 6. Cancel Ticket Tab
        print("Navigating to Cancel Ticket tab...")
        page.click("#cancel-tab")
        page.wait_for_selector("#searchPnr", state="visible")
        page.fill("#searchPnr", pnr)
        page.click('button[onclick="searchTicket()"]')
        page.wait_for_selector("#ticket-details", state="visible", timeout=5000)
        time.sleep(0.5)

        print("Clicking Cancel Ticket & Refund...")
        page.click('button[onclick^="confirmCancel"]')
        # Wait for cancellation success message/alert in alert-container
        time.sleep(1.5)

        cancelled_ticket_path = os.path.join(screenshot_dir, "6_cancelled_ticket.png")
        page.screenshot(path=cancelled_ticket_path)
        print(f"Saved Cancelled Ticket screen to {cancelled_ticket_path}")

        browser.close()
        print("Screenshots captured successfully!")

if __name__ == "__main__":
    run()
