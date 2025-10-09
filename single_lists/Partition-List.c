/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 void print_list(struct ListNode* head) {
    printf("\n List:");
    while (head) {
        printf(" %d ", head->val);
        head = head->next;
    }
 }

struct ListNode* partition(struct ListNode* head, int x) {

    if (head==NULL || head->next==NULL) return head;

    struct ListNode *new_head=NULL, *curr_less=NULL, *curr_more=NULL, *half_head=NULL;
    bool flag_less = 1, flag_more = 1;

    while(head) {        
        if (head->val < x) {
            if (flag_less) {
                new_head = head;
                curr_less = new_head;
                flag_less = 0;                
                //printf("\n inside flag_less ");
                //print_list(new_head);
            } else {
                curr_less->next = head;
                //printf("\n else less curr_less=%d", curr_less->val);
                //printf("\n else less curr_less=%d", curr_less->next->val);
                curr_less = curr_less->next;
                if (curr_less->next == NULL) {
                    curr_less->next = NULL;
                    if (curr_more) curr_more->next = NULL;                   
                    //printf("\n here less");
                    break;
                }
                //printf("\n inside flag_less ");
                //print_list(new_head);            
            }
        } else {
            if (flag_more) {
                half_head = head;
                curr_more = half_head;
                flag_more = 0;
                //printf("\n inside flag_more ");
                //print_list(half_head);
            } else {
                //printf("\n +++ curr_more=%d", curr_more->val);
                curr_more->next = head;
                curr_more = curr_more->next;//printf("\n ---- curr_more=%d", curr_more->val);
                //print_list(half_head);
                if (curr_more->next == NULL) {
                    if (curr_less) curr_less->next = NULL;
                    curr_more->next = NULL;
                    //printf("\n here more");
                    break;
                } 
                //printf("\n inside flag_more ");
                //print_list(half_head);                
            }
        }
        //printf("\n before exit head=%d", head->val);
        head = head->next;
        //if (head) printf("\n starting with head=%d", head->val);
    }
/*    
if (new_head) printf("\n out new_head=%d", new_head->val);
if (half_head) printf("\n out half_head=%d", half_head->val);
if (curr_less) printf("\n out curr_less=%d", curr_less->val);
if (curr_more) printf("\n out curr_more=%d", curr_more->val);
*/
    if(curr_more) curr_more->next = NULL;
//print_list(new_head);
//print_list(half_head);
    if (new_head == NULL) return half_head;
    curr_less->next = half_head;

return new_head;

}