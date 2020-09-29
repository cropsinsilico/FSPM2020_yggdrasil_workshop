
light <- function(height, time) {
  intensity <- 80.0 * (1.0 + sin(2.0 * pi * time / 365)) / (abs(200 - height)**2)
  return(intensity)
}