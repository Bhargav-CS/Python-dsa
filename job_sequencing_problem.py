class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def JobScheduling(self, Jobs, n):
        # Sort jobs by profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Find maximum deadline to determine the size of the parent array
        maxDeadline = max(job.deadline for job in Jobs)

        # Initialize the parent array with each index pointing to itself
        parent = list(range(maxDeadline + 1))

        def find(parent, i):
            if parent[i] == i:
                return i
            parent[i] = find(parent, parent[i])
            return parent[i]

        totalProfit = 0
        countJobs = 0

        # Iterate over the sorted jobs
        for job in Jobs:
            # Find the latest available slot for this job
            if countJobs == maxDeadline:
                break
            availableSlot = find(parent, job.deadline)

            # If a valid slot is found, schedule the job
            if availableSlot > 0:
                parent[availableSlot] = find(parent, availableSlot - 1)  # Union step
                totalProfit += job.profit
                countJobs += 1

        return [countJobs, totalProfit]

# Example usage
Jobs = [Job(1, 4, 20), Job(2, 1, 1), Job(3, 1, 40), Job(4, 1, 30)]
sol = Solution()
print(sol.JobScheduling(Jobs, len(Jobs)))  # Output: [2, 60]