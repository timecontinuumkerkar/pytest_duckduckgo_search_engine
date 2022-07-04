import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    # Initialize webdriver
    b = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Adding wait for all the test cases and lines
    b.implicitly_wait(10)

    # Return the webdriver instance
    yield b

    # Quit the browser but don't close it
    b.quit()
