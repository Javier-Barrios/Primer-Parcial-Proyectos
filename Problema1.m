x=randi([1,6],1,1)
y=randi([1,6],1,1)
z=x+y
if z==8
  disp('Ganaste')  
elseif z==7
  disp('Perdiste')
elseif z~=8 & z~=7
  disp('Sigue Participando')
else 
  disp('Sigue Participando')
end
