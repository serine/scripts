		#-------------------------------------------------------
		# This section is specific for columns name formating
		#-------------------------------------------------------

		fileAsStr = str(f)
		tmpName = fileAsStr.split("/")[-1]
		
		if tmpName.startswith("cf"):

			tmpRoot = tmpName.split("_")
			tmp1 = tmpRoot.pop()
			tmp2 = tmpRoot.pop()
			rootName  = ''.join(tmpRoot)
			sampleId = str(rootName.split("-")[1])

		else:

			tmpRoot = tmpName.split("_")
			sampleId = str(tmpRoot[0])
		#-------------------------------------------------------
