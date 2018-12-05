import graphics

def main():
	windowName = "Anime Renaming Utility ~ (A.R.U.)"
	windowX = 400
	windowY = 400
	window = graphics.GraphWin(windowName, windowX, windowY)
	window.setBackground(graphics.color_rgb(17, 17, 29))

	lineX = graphics.Line(graphics.Point(0, 280), graphics.Point(400, 280))
	lineX.setFill("white")
	lineX.draw(window)
	lineY = graphics.Line(graphics.Point(130, 0), graphics.Point(130, 400))
	lineY.setFill("white")
	lineY.draw(window)

	nameLabel = graphics.Text(graphics.Point(60, 40), "Name:")
	nameControl = graphics.Entry(graphics.Point(260, 40), 25)
	seasonLabel = graphics.Text(graphics.Point(60, 100), "Season:")
	seasonControl = graphics.Entry(graphics.Point(160, 100), 3)
	episodesLabel = graphics.Text(graphics.Point(60, 160), "Episodes:")
	episodesControl = graphics.Entry(graphics.Point(160, 160), 3)
	startLabel = graphics.Text(graphics.Point(60, 220), "RENAME")
	startButton = graphics.Rectangle(graphics.Point(20, 205), graphics.Point(100, 235))
	resultLabel = graphics.Text(graphics.Point(60, 340), "0 of 0:")
	resultControl = graphics.Entry(graphics.Point(260, 340), 25)
	leftButton = graphics.Rectangle(graphics.Point(5, 370), graphics.Point(30, 395))
	rightButton = graphics.Rectangle(graphics.Point(100, 370), graphics.Point(125, 395))
	
	nameLabel.setTextColor("white")
	nameControl.setFill("white")
	seasonLabel.setTextColor("white")
	seasonControl.setFill("white")
	episodesLabel.setTextColor("white")
	episodesControl.setFill("white")
	startLabel.setTextColor("white")
	startButton.setFill("green")
	resultLabel.setTextColor("white")
	#resultControl.setFill("white")
	leftButton.setFill("white")
	rightButton.setFill("white")

	seasonLabel.draw(window)
	seasonControl.draw(window)
	episodesLabel.draw(window)
	episodesControl.draw(window)
	startButton.draw(window)
	startLabel.draw(window)
	resultLabel.draw(window)
	resultControl.draw(window)
	nameLabel.draw(window)
	nameControl.draw(window)

	name = ""
	season = 0
	episodes = 0
	clearMode = False
	displayed = 0

	while True:
		click = window.checkMouse()
		key = window.checkKey()

		if detect_start(startButton, click, key):
			if clearMode:
				nameControl.setText("")
				seasonControl.setText("")
				episodesControl.setText("")
				resultControl.setText("")

				displayed = 0
				episodes = 0
				resultLabel.setText(str(displayed) + " of " + str(episodes))

				leftButton.undraw()
				rightButton.undraw()

				startButton.undraw()
				startLabel.undraw()
				startButton.setFill("green")
				startLabel.setText("RENAME")
				startButton.draw(window)
				startLabel.draw(window)

				clearMode = False
			else:
				startButton.undraw()
				startLabel.undraw()
				startButton.setFill("red")
				startLabel.setText("CLEAR")
				startButton.draw(window)
				startLabel.draw(window)

				leftButton.draw(window)
				rightButton.draw(window)

				season = seasonControl.getText()
				episodes = get_episodes(episodesControl)
				if episodes > 0:
					displayed = displayed + 1

				resultLabel.setText(str(displayed) + " of " + str(episodes))
				resultControl.setText("The result will be displayed here.")
				clearMode = True

		if clearMode:
			if detect_left(leftButton, click, key) and displayed > 1:
				displayed = displayed - 1
				resultLabel.setText(str(displayed) + " of " + str(episodes))
				resultControl.setText("The result will be displayed here.")
			elif detect_right(rightButton, click, key) and displayed < episodes:
				displayed = displayed + 1
				resultLabel.setText(str(displayed) + " of " + str(episodes))
				resultControl.setText("The result will be displayed here.")

	return


def detect_start(button, click, key):
	if click:
		cX = click.getX()
		cY = click.getY()
		bX1 = button.getP1().getX()
		bX2 = button.getP2().getX()
		bY1 = button.getP1().getY()
		bY2 = button.getP2().getY()
		if bX1 < cX < bX2 and bY1 < cY < bY2:
			return True

	if key == 'Return':
		return True

	return False


def detect_left(button, click, key):
	if click:
		cX = click.getX()
		cY = click.getY()
		bX1 = button.getP1().getX()
		bX2 = button.getP2().getX()
		bY1 = button.getP1().getY()
		bY2 = button.getP2().getY()
		if bX1 < cX < bX2 and bY1 < cY < bY2:
			return True
		return False


def detect_right(button, click, key):
	if click:
		cX = click.getX()
		cY = click.getY()
		bX1 = button.getP1().getX()
		bX2 = button.getP2().getX()
		bY1 = button.getP1().getY()
		bY2 = button.getP2().getY()
		if bX1 < cX < bX2 and bY1 < cY < bY2:
			return True
		return False


def get_episodes(control):
	episodes = control.getText()
	if episodes == '' or int(episodes) < 1:
		return 0

	return int(episodes)


main()
