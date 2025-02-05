Feature: Validate Dropdown Column Navigation and Page Access

    @smoke_test
    @regression_tests
    Scenario: Validate menu options
        Given I navigate to the kayak main page
        Then I should be in the "home" page
        And The url page should be equal to the next "https://www.kayak.com.co/" url
        Then The "home_message" "label" should contain the "Compara ofertas de vuelos en cientos de webs" text
        When I click on the "menu" "button"
        And I click on the "menu_stays" "button"
        #Then I should be in the "stays" page
        Then The "stays_message" "label" should contain the "Compara ofertas de hoteles en cientos de webs" text

        When I click on the "menu" "button"
        And I click on the "menu_cars" "button"
        #Then I should be in the "cars" page
        Then The "cars_message" "label" should contain the "Compara ofertas de alquiler de carros en cientos de webs" text

        When I click on the "menu" "button"
        And I click on the "menu_explore" "button"
        #Then I should be in the "explore" page
        Then The "scale_message" "label" should contain the "Hasta 1 escala" text

        When I click on the "menu" "button"
        And I click on the "menu_news" "button"
        #Then I should be in the "news" page
        Then The "read_more" "label" should contain the "Leer más" text
        When I click on the "logo" "button"
        Then I should be in the "home" page

        When I click on the "menu" "button"
        And I click on the "menu_direct" "button"
        #Then I should be in the "direct" page
        Then The "direct_message" "label" should contain the "Vuelos directos desde Bogotá, Colombia - El Dorado (BOG)" text

        When I click on the "menu" "button"
        And I click on the "menu_moment" "button"
        #Then I should be in the "moment" page
        Then The "moment_message" "label" should contain the "Descubre cuándo reservar tu próximo viaje." text

        When I click on the "menu" "button"
        And I click on the "menu_business" "button"
        #Then I should be in the "business" page
        Then The "business_message" "label" should contain the "Viaje de negocios. Sin complicaciones." text

        When I click on the "menu" "button"
        And I click on the "menu_trips" "button"
        #Then I should be in the "trips" page
        Then The "trips_message" "label" should contain the "Una forma más fácil de gestionar tus viajes" text

        When I click on the "menu" "button"
        And I click on the "menu_flights" "button"
        #Then I should be in the "flights" page
        Then The "home_message" "label" should contain the "Compara ofertas de vuelos en cientos de webs" text