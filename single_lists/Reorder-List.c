/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 struct ListNode* tail(struct ListNode* node){
    while(node->next->next != NULL) {
        node = node->next;
        //printf("\n node->val = %d", node->val);
    }

    return node;
 }
void reorderList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) exit;

struct ListNode *slow=head, *fast=head;
bool odd = 0;

    while (fast->next != NULL) {
        fast = fast->next;
        if (fast->next != NULL) {
            fast = fast->next;
            slow = slow->next;
        }
    }

    //printf ("\n slow = %d, fast = %d", slow->val, fast->val);
//reverse the second part of the list

struct ListNode *prev, *curr, *next, *head_second;
prev = NULL;
curr = slow->next;
next = slow->next;
head_second = curr;
//if (head_second )printf ("\n head_second = %d", head_second->val);

//close the first half of the original list
slow->next = NULL;

    while(next != NULL) {
        //printf("\n ---");
        next = next->next;  //if(next)printf ("\n next = %d", next->val);
        curr->next = prev;
        prev = curr;  //printf ("\n prev = %d", prev->val);
        curr = next;  //if (curr) printf ("\n curr = %d", curr->val);
        head_second = prev;
        if (curr == NULL) break;
    }
/*
    while (head_second) {
        printf("\n .  %d   ", head_second->val);
        head_second =head_second->next;
    }
*/
    //merging the two lists
    struct ListNode *head_first = head, *next_first = head, *next_second= head_second;
//printf("\n .  l1=%d l1_n=%d l2=%d   ", head_first->val, next_first->val, head_second->val);
    while(head_first  && head_second ) {
        next_first = head_first->next; 
        next_second = head_second->next;
        head_first->next = head_second;
        head_second->next = next_first;
        head_first = next_first;
        head_second = next_second; 
        //if(head_first) printf("\n .  head_first = %d   ", head_first->val); 
        //if (head_second) printf("\n .  head_second = %d",  head_second->val); 
    }

/*
    while (head->next!=NULL) {
        pre_last = tail(head);//printf("\n pre_last->val = %d", pre_last->val);
        if (head->next == pre_last->next) break;
        next = head->next;//printf("\n next->val = %d", next->val);
        head->next = pre_last->next;
        pre_last->next->next = next;
        pre_last->next = NULL;
        head = next;//printf("\n head->val = %d", head->val);
    }
*/

}