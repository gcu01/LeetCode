/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 void print_list(struct ListNode *head) {
    printf("\n Listing:");
    while(head) {
        printf(" %d ", head->val);
        head = head->next;
    }
 }

 bool compare_lists(struct ListNode *head1, struct ListNode* head2) {
    while(head1) {
        if(head1->val != head2->val) return 0;
        if ((head1->next != NULL && head2->next == NULL) || (head2->next != NULL && head1->next == NULL)) return 0;
        head1 = head1->next;
        head2 = head2->next;
    }

    return 1;
 }

 struct ListNode* inverse_me(struct ListNode *head) {
    struct ListNode *prev = NULL, *curr = head, *next = head, *new_head = NULL;

    while(curr) {
        next = next->next;
        curr->next = prev;
        new_head = curr;        
        prev = curr;
        curr = next;
    }

    //print_list(new_head);
    return new_head;
 }

bool isPalindrome(struct ListNode* head) {
    if (head == NULL ) return 0;
    if (head->next == NULL) return 1;
    //inverse_me(head);

    struct ListNode *slow = NULL, *fast = NULL, *curr = NULL, *first_head = NULL, *half_head = NULL;
    bool jump = 1;
    int idx_fast = 1, idx_slow = 1;

    slow = fast = curr = head;
    while (fast->next) {
        if (jump) {
            fast = fast->next;
            idx_fast++;
            jump = 0;
        } else {
            slow = slow->next;
            fast = fast->next;
            idx_slow++;
            idx_fast++;
            jump = 1;
        }
        curr = curr->next;
    }
//printf("\n slow = %d", slow->val);
//printf("\n fast = %d", fast->val);
    half_head = slow->next;
//print_list(half_head);
    slow->next = NULL;
    first_head = inverse_me(head);
//print_list(first_head);
//printf("\n idx_slow = %d, idx_fast = %d", idx_slow, idx_fast);
    if (idx_fast%2 == 0) {
        return compare_lists(first_head, half_head);
    } else {
        return compare_lists(first_head->next, half_head);
    }


}    




















// my solution is working but takes too much
/*
bool isPalindrome(struct ListNode* head) {
    bool out = 0; //is not palindrom
    if (head == NULL) {
        return 0;
    } else if (head->next == NULL) return 1;
//printf("head->next = %p",head->next);
    struct ListNode *end=head, *prev=NULL;
    int count = 0;

    while(end->next!=NULL) {
        prev = end;
        end = end->next;
        count++;
    }
    if (head->val == end->val) {
        head = head->next;
        end = prev;
        prev = head;
        out = 1;
    } else {return 0;}
    if (count == 1)  return 1;

    while (head!=end){
        while(prev->next!=end) {
            prev = prev->next;
        } 
        if (head->val == end->val) {
            if (head->next == end) return 1;
            head = head->next;
            end = prev;
            prev = head;
        } else {
            return 0;
        } 
    }

    return out;
}
*/