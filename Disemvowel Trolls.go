// Codewars
package kata

import "strings"

func Disemvowel(comment string) string {
  vols := "aeuio"
  for _, el := range vols{
    if strings.Contains(strings.ToLower(string(el)), vols){
      comment = strings.Replace(comment, string(el), "", 1)
    }
  }
  return comment
}
