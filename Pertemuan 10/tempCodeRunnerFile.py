def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)
