/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

 int greatest(struct ListNode* head, int value) {
    //printf("\n inside function value=%d", value);
    while (head) {
        if (head->val > value) {
            //printf("\n max=%d", head->val);
            return head->val;
        }
        head = head->next;
    }
//printf("\n max=%d", 0);
    return 0;
 }
int* nextLargerNodes(struct ListNode* head, int* returnSize) {    

    int *output=NULL, size=0, capacity=2;
    struct ListNode *curr=head, *node=head;
    output = (int*) malloc(capacity*sizeof(int));
    while (curr) {
        //printf("\n size=%d", size);
        if (size >= capacity) {
            
            capacity *= 2;
            //printf("\n size>capacity new_capacity=%d", capacity);
            int *temp = (int *) realloc(output, capacity*sizeof(int));
            output = temp;
            //printf("\n output[1]=%d", output[1]);
        }
        if (curr->next) {
            output[size] = greatest(curr->next, curr->val);
        } else {
            output[size] = 0;
            //printf("\n output[2]=%d", output[2]);
        }
        curr = curr->next;
        size++;
    }   
    *returnSize = size;
    //for(int i=0; i<size; i++) printf("\n output[%d]=%d", i, output[i]);

    return output;
}