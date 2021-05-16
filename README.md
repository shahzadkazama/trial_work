# trial_project

# Requirement
 - docker
 - docker-compose


1- clone the project

   git clone https://github.com/shahzadkazama/trial_work.git
   
2- execute the project

  cd trial_work
  docker-compose up -d --build

3- verify the services
  docker-compse ps

4- how to add a car by post request only, you can use postman or any api tool

   http://your-ip-address/trail/add_car/

   car_type=suvs
   car_model=2017
   car_make=kia
   car_price=550000
   car_year=2021

5- how to find a car by post request,  enter the car_id
   http://your-ip-address/trail/find_car/
   
   car_id = 1
