extends KinematicBody2D

var move_speed=480
var jump_jump=-720
var gravity= 1200
var velocity= Vector2.ZERO
var esta_no_chao
onready var raycasts = $Raycasts

func _physics_process(delta):
	velocity.y += gravity*delta
	velocity= move_and_slide(velocity)
	_se_mover()
	_definir_animacao()
	esta_no_chao= _chegar_se_ta_no_cha()


func _se_mover():
	velocity.x= 0
	
	var move_direction= int(Input.is_action_pressed("move_right")) - int(Input.is_action_pressed("move_left"))
	velocity.x= lerp(velocity.x, move_speed*move_direction,0.2)
	
	if move_direction != 0:
		$Sprite.scale.x = move_direction


func _definir_animacao():
	var animacao= "Idle"
	
	if esta_no_chao== false:
		animacao= "Jump"
	elif velocity.x != 0:
		animacao= "Run"
		
		
	if $AnimationPlayer.assigned_animation !=animacao:
		$AnimationPlayer.play(animacao)

func _input(event):
	if event.is_action_pressed("jump") and esta_no_chao== true:
		velocity.y = jump_jump / 2

func _chegar_se_ta_no_cha():
	for raycast in raycasts.get_children():
		if raycast.is_colliding():
			return true
	return false

