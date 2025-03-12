cmake_minimum_required(VERSION 3.8)
project(sza_i5e_teknos)

# Találd meg az ament_cmake és ament_cmake_python csomagokat
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(turtlesim REQUIRED)

# Telepítendő Python scriptek
install(
  PROGRAMS
  src/szivrajz.py  # Az abszolút elérési utat használjuk
  DESTINATION lib/${PROJECT_NAME}
)


# Telepítendő launch fájlok
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

