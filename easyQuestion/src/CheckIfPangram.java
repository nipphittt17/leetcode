//1832. Check if the Sentence Is Pangram

public class CheckIfPangram {
    public static boolean checkIfPangram(String sentence) {
        
        int[] countAlpha = new int[26];
        
        for(int i = 0 ; i < sentence.length() ; i++){
            int index = (int)sentence.charAt(i);
            countAlpha[index-97]++;
        }

        for(int i = 0 ; i < countAlpha.length ; i++){
            if(countAlpha[i] == 0) return false;
        }

        return true;
        
    }

    public static void main(String[] args) {
        String sentence = "thequickbrownfoxjumpsoverthelazydog";
        boolean test1 = checkIfPangram(sentence);
        System.out.println(test1);
    }
}
