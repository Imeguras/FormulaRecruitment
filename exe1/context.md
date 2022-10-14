# Before running

Install OpenCV

# What have you done!?!

Well this is a badly written automatic multithreaded birds eye view for paper, that is you put in a piece of paper on a desk, tilt your camera so that the paper is seen and it will do a birds eye view of the paper. The program uses various threads to be able to keep up with expensive operations(like drawing on the screen, saturation, finding polygons, etc...)

The problem is that i thought multithreading wouldnt complicate matters until i rechecked the exercise and then the mess that it is started happening

## It doesnt even work!

To detect the paper(or the surface) 4 conditions must be met, it has to be a 4 sided polygon(regular or irregular), it should be somewhat big, it has to have contrast(higher equals better), and it should be light colored(i imagined that the paper would never be black so the low colours are cut).

Then you are supposed to click in the center, the algorithm will then fetch the 4 closest points to your mouse click and proceed to do a bird eye view of that area.

## No "manual mode"? 

i intended to so... but the code is very spaggeti, if needed i will promply rewrite everything from scratch and start building everything in paper

## how do i... EXIT!?

press q... or esc... it depends
