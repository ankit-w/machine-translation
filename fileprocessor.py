with open("small_vocab_en") as xh:
  with open('small_vocab_fr') as yh:
    with open("en_fr","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists
      #combine = list(zip(ylines,xlines))
      #Write to third file
      for i in range(len(xlines)):
        line = ylines[i].strip() + '\t' + xlines[i]
        zh.write(line)