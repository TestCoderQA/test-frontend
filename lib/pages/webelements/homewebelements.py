from selenium.webdriver.common.by import By


class HomeWebElements:
    #where_label = (By.CSS_SELECTOR, '.primary-content h2')
    where_label = (By.CSS_SELECTOR, '#main-search-form > section > div > div > div > div.W5IJ-mod-limit-width > h2 > span:nth-child(1)')

    #signin_button = (By.CSS_SELECTOR, '.menu__wrapper .menu-label__wrapper button')
    signin_button = (By.CSS_SELECTOR, 'div.ZGw-.ZGw--mod-size-medium span.J-sA-label')

    #search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    search_button = (By.CSS_SELECTOR, 'div.W5IJ-mod-limit-width button')

    name_tag_input = (By.XPATH, '//input[contains(@placeholder, "Origen") or contains(@aria-label, "Origen")]')
    name_dropdown_column_input = (By.XPATH, '//div[@role="combobox" and @aria-label="Tipo de viaje Ida y vuelta"]')
    search_tag_button = (By.XPATH, '//button[@type="submit" and @aria-label="Buscar"]')
    cancel_button = (By.XPATH, '//div[@role="button" and @aria-label="Remove value"]')
    logo_button  = (By.XPATH, '//a[contains(@class, "logo-link")]')

    # left menu selectors
    menu_button = (By.XPATH, '(//div[@role="button" and contains(@class, "ZGw-")])[1]')
    menu_flights_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Vuelos"]')
    menu_stays_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Alojamientos"]')
    menu_cars_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Carros"]')
    menu_explore_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Explore"]')
    menu_news_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Blog"]')
    menu_direct_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Vuelos directos"]')
    menu_moment_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="El mejor momento"]')
    menu_business_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="KAYAK for Business"]')
    menu_trips_button = (By.XPATH, '//a/div[contains(@class, "dJtn-menu-item-title") and text()="Trips"]')


    # main tags of each page
    home_message_label = (By.XPATH, '//h2//span[contains(text(), "Compara ofertas de vuelos")]')
    stays_message_label = (By.XPATH, '//h2//span[contains(text(), "Compara ofertas de hoteles")]')
    cars_message_label = (By.XPATH, '//h2//span[contains(text(), "Compara ofertas de alquiler de carros")]')
    scale_message_label = (By.XPATH, '//label[span[contains(text(), "Hasta 1 escala")]]')
    read_more_label = (By.XPATH, '(//a[contains(text(), "Leer más")])[1]')
    direct_message_label = (By.XPATH, '//h2[contains(text(), "Vuelos directos desde")]')
    moment_message_label = (By.XPATH, '//h1[text() = "Descubre cuándo reservar tu próximo viaje."]')
    business_message_label = (By.XPATH, '//h1[text() = "Viaje de negocios."]')
    trips_message_label = (By.XPATH, '//h1[contains(text(), "Una forma más fácil de gestionar tus viajes")]')