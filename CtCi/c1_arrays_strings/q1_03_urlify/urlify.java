// Example from the book


package q1_03_urlify;
public class urlify {
  
  void replaceSpaces(char[] str, int trueLength) {
    int spaceCount = 0, index, i = 0;
    
    // Count spaces within the true length
    for (i = 0; i < trueLength; i++) {
      if (str[i] == ' ') {
        spaceCount++;
      }
    }
    
    index = trueLength + spaceCount * 2; // it is done, so because we are replacing a space with %20, so 2 extra characters are needed for every space
    // Ensure the array has enough space
    if (trueLength < str.length) str[trueLength] = '\0';
    
    for (i = trueLength - 1; i >= 0; i--) {
      if (str[i] == ' ') {
        str[index - 1] = '0';
        str[index - 2] = '2';
        str[index - 3] = '%';
        index = index - 3;
      } else {
        str[index - 1] = str[i];
        index--;
      }
    }
  }
  
  public static void main(String[] args) {
    urlify urlify = new urlify();
    String input = "Mr John Smith    "; // String with enough buffer at the end
    int trueLength = 13;
    char[] charArray = input.toCharArray();
    
    urlify.replaceSpaces(charArray, trueLength);
    
    System.out.println(new String(charArray));
  }
}