# Travel Agent Chatbot - BoBo
By: Haasitha Pidaparthi

This chatbot is build using Rasa Platform

Rasa Installation:
https://rasa.com/docs/rasa/installation

Prequisites: 
* Anaconda installed

### **How to set up this project:**
* Download the github project into your local system. 
* With in the created virtual environment:
  * Install Rasa using the dependencies found in the dependency.txt file
  * Optional: Install Rasa X (for better UI experience)
 ```
 pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
 ```

### **How to run the chatbot:**

In the virtual environment, open the project and run the following commands on the terminal:
* Train the chatbot
  ```
  rasa train
  ```
* Open a separate terminal and start the action server
  ```
  rasa run actions
  ```
* Chat with the bot using rasa shell or rasa x
  ```
  rasa shell
  ```
  ```
  rasa x
  ```
    
 ## Conversation Flow 1: Plan My Trip
 user: hi
 
 bot: Hello Traveler!
      Welcome to Bora Bora, the Jewel of the South Seas! I am BoBo, a Travel-Agent Bot here to guide you to make the best of your Bora Bora trip.
 
 user: ok
 
 bot: I am excited to assist you with your travel arrangements.
 
 bot: Are you ready to experience a tropical paradise? Here are some options you can choose from:
   * Plan My Trip
   * About Bora Bora Island
   * Activities Offered
   * Contact Us
 
 user: plan my trip
 
 bot: Great! Lets get started! What package would you like to choose? Here are our available options:
   - family
   - vacation
   - honeymoon
   - cruise
   - adventure
   - wedding
   - luxury
   - festivals and events
   - special
 
 user: vacation
 
 bot: You can choose to plan your trip on any of the island below:
   - bora bora
   - tahiti
   - moorea
   - huahine
   - raiatea
 
 user: tahiti
 
 bot: How many people is this trip for?
   - 1
   - 2
   - 3
   - 4
   - 5+
 
 user: 3
 
 bot: How long do you want to stay for your trip?
   - no limit
   - two days
   - five days
   - one week
   - two weeks
 
 user: no limit
 
 bot: What is your budget?
   - any
   - under $3000
   - $3000-$5000
   - over $5000
 
 user: any
 
 bot: The form is successfully submitted! We can't wait to see you at the Islands!
 
 bot: Here's a summary of your choices:
   - Package: vacation
   - Island: tahiti
   - Number of People: 3
   - Number of Nights: no limit
   - Budget: any
 
 user: thank you
 
 bot: You are welcome!
 
 ## Conversation Flow 2: About Bora Bora
 user: hi
 
 bot: Hello Traveler!
      Welcome to Bora Bora, the Jewel of the South Seas! I am BoBo, a Travel-Agent Bot here to guide you to make the best of your Bora Bora trip.
 
 user: ok
 
 bot: I am excited to assist you with your travel arrangements.
 
 bot: Are you ready to experience a tropical paradise? Here are some options you can choose from:
   - Plan My Trip
   - About Bora Bora Island
   - Activities Offered
   - Contact Us
 
 user: about bora bora
 
 bot: https://www.conradboraboranuiresort.com/wp-content/uploads/2019/04/resort-exterior-1920x1200-1-1024x640.jpg
      Bora Bora is a small South Pacific island northwest of Tahiti in French Polynesia. Surrounded by sand-fringed motus (islets) and a turquoise lagoon protected       by a coral reef, it’s known for its scuba diving. It's also a popular luxury resort destination where some guest bungalows are perched over the water on    
      stilts.
 
 user: Wow!
 
 ## Conversation Flow 2: Activities Offered
 user: hi
 
 bot: Hello Traveler!
      Welcome to Bora Bora, the Jewel of the South Seas! I am BoBo, a Travel-Agent Bot here to guide you to make the best of your Bora Bora trip.
 
 user: ok
 
 bot: I am excited to assist you with your travel arrangements.
 
 bot: Are you ready to experience a tropical paradise? Here are some options you can choose from:
   - Plan My Trip
   - About Bora Bora Island
   - Activities Offered
   - Contact Us
 
 user: activities offered
 
 bot: https://www.tahitilegends.com/images1/gallery/BOB-Natura-Discvoery-Cultural-Tour-1200x720_53223.jpg
      Island Tour
      Circle the island with your professional and experienced guide. 
      Learn the island's legends, discover the American WWII cannons, 
      visit an ancient temple, and meet a local family who will serve you 
      fruit from their plantation. You will also visit villages where you 
      will learn how to make your own sarong and discover the local fauna 
      of the island as well as several vistas with breathtaking views. 
      Private tours available as well.
      
 user: more
 
 bot: https://www.tahitilegends.com/images1/gallery/BOB-Shark-and-Ray-1200x720_19753.jpg
      Eco Shark & Ray Snorkel Safari
      Arrive at a vibrant coral garden where you'll have the opportunity to 
      snorkel in clear and shallow waters. Your guide will then take you to 
      feed the sharks and stingrays. You'll be able to get in the water and 
      swim with them or simply watch from the boat.
 
 user: what else do you have?
 
 bot: https://www.tahitilegends.com/images1/gallery/BOB-Bloody-Marys-1200x720_21303.jpg
      Dinner at the World-Famous Bloody Mary's
      Experience an evening at the famous Bloody Mary's restaurant.  Often 
      frequented by celebrities, Blood Mary's is known for its fresh food, 
      signature cocktails and great ambiance.  You'll enjoy the catch of the 
      day prepared to your liking, or choose from a selection of fresh dishes 
      including crab, shrimp, steak, chicken, and vegetarian options.
 
  user: show me more?
  
  bot: https://www.tahitilegends.com/images1/gallery/BOB-Aqua-Safari-1200x720_20013.jpg
       Aqua Safari with Helmet
       Go for a walk underwater with an air-supplied helmet and find yourself 
       surrounded by tropical fish. This 2-hour excursion includes a boat tour 
       of Bora Bora and snorkeling in the lagoon. This activity is not permitted 
       for pregnant women, people with asthma, or anyone unable to walk. Transfers 
       Included for all resorts except the Four Seasons.
  
  user: what else?
  
  bot: https://www.tahitilegends.com/images1/gallery/Bora-Bora-Lagoon-Cruise-Raanui-Tours3-1200x720_19723.jpg
       Full Day Lagoon Cruise & Motu Tahitian Barbecue
       Enjoy an unforgettable day as you circle the island of Bora Bora by boat 
       with a representative of Raanui Tours. You'll snorkel in the beautiful 
       coral gardens, watch the graceful stingrays in their natural environment, 
       and get up close and personal with black tipped reef sharks. This excursion 
       includes a stop at motu Tapu for a traditional Tahitian barbecue.
  
  user: tell me more
  
  bot: We are adding more options, but these are all we have for now.
  
## Conversation Flow 2: Contact Us
 user: hi
 
 bot: Hello Traveler!
      Welcome to Bora Bora, the Jewel of the South Seas! I am BoBo, a Travel-Agent Bot here to guide you to make the best of your Bora Bora trip.
 
 user: ok
 
 bot: I am excited to assist you with your travel arrangements.
 
 bot: Are you ready to experience a tropical paradise? Here are some options you can choose from:
   - Plan My Trip
   - About Bora Bora Island
   - Activities Offered
   - Contact Us
 
 user: contact us
 
 bot You can contact our operations team at 123-456-7890.
 
 user: what are your hours?
 
 bot: We are open Monday-Friday between 8am to 5pm! But I am always here for assistance :)
      
