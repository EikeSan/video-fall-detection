# video-fall-detection
OpenCv project to detect a person fall in videos with haarcascade

# Prerequesite
Packages used:
- python==2.7.7
- numpy==1.14.5
- opencv-python==3.4.1.15
- pylint==1.9.2
- scikit-learn==0.19.1

# How it works
For each frame readed of the video corverted into gray, is removed the background, finded the contour and drawed the contours.
If the heigh of the contour is lower than width, it may be a fall and we add 1 to a count, if the count is greater than 10, will be drawed a rectangle to the possible person fallen.

# How to contribute
To contribute to this project make the following guide:
- Fork this repository, It will create a copy of the repository into  your account.
- Clone the forked repository. (`git clone https://github.com/my-user/video-fall-detection.git`)
- Create your awesome code!
- Commit and push the changes.
- Create a pull request via Github. (Go to the forked repo and press the `Pull request` button)

Fell free to contribute ;)
