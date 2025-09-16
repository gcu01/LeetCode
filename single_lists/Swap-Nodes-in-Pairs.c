/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if (head == NULL || head->next == NULL ) return head;

struct ListNode *new_head, *curr, *prev, *p_prev;

curr = head->next;
new_head = curr;
prev = head;
prev->next = curr->next;
curr->next = prev;
p_prev = prev;
//printf("\n curr->val =%d, prev->val = %d ", curr->val, prev->val);

while (prev->next != NULL && prev->next->next != NULL) {
    curr = prev->next->next;
    prev = prev->next;
    //printf("\n while1  curr->val =%d, prev->val = %d p_prev->val = %d", curr->val, prev->val, p_prev->val);
    p_prev->next = curr;
    //printf("\n while2  p_prev->val = %d",  p_prev->val);
    //printf("\n while3  curr->val =%d, prev->val = %d p_prev->val = %d", curr->val, prev->val, p_prev->val);
    prev->next = curr->next;
    curr->next = prev;
    p_prev = prev;
}

return new_head;

/*

new_head = head->next;
printf("\n new_head->val = %d ", new_head->val);
head->next->next = prev;
prev = head;

head->next = head->next->next;
printf("\n head->next->val = %d", head->next->val);
curr = head->next;
printf("\n curr->val =%d, prev->val = %d ", curr->val, prev->val);
printf("\n curr->val =%d, prev->val = %d ", curr->val, prev->val);
*/
/*
while (curr != NULL || curr->next != NULL) {
    curr->next = curr->next->next;
    prev = curr;
    prev->next = curr->next;
    curr->next->next = curr;
    curr = curr->next;
}
*/


/*
    struct ListNode *new_head = head->next, *prev= head, *last2;
    int n = 0;
    printf("\n init head = %p, head->next = %p, head->next->next = %p head->next->next->next = %p", head, head->next, (head->next)->next, (head->next)->next->next);
    
    head = head->next;
    prev->next = head->next;
    head->next = prev;

    if (head->next != NULL ) {
        last2 = head;
        head = prev->next;
        prev = head;
        //last2->next = head;
        if (head->next != NULL ) printf("\n after 1st head = %p, head->next = %p, head->next->next = %p, prev = %p", head, head->next, (head->next)->next, prev);
        printf("\n  after 1st new_head = %p, head->next = %p, head->next->next = %p, head->next->next = %p, prev = %p head=%p", new_head, new_head->next, (new_head->next)->next, (new_head->next)->next->next ,prev, head);
    }


    while( head->next != NULL ) {
        printf("\n while1  head = %p, head->next = %p, head->next->next = %p, prev = %p last2=%p", head, head->next, (head->next)->next ,prev, last2);
        //if ( head->next != NULL ) {
            head = head->next;
            prev->next = head->next;
            head->next = prev;
            last2->next = head;
    printf("\n while2  head = %p,  prev = %p", head, prev);
    printf("\n middle new_head = %p, head->next = %p, head->next->next = %p, head->next->next = %p, prev = %p", new_head, new_head->next, (new_head->next)->next, (new_head->next)->next->next ,prev);
                if (prev->next != NULL ) {
                    last2 = head;
                    head = prev->next;
                    prev = head;
                }
    printf("\n while22  head = %p,  prev = %p", head, prev);
    printf("\n end head = %p, head->next = %p, head->next->next = %p, head->next->next = %p, prev = %p", new_head, new_head->next, (new_head->next)->next, (new_head->next)->next->next ,prev);
        //} else 
        //    head = head->next;
    }


   return new_head;

*/
}